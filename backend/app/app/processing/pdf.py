import re

import PyPDF2

from app.models.settings import Settings
from app.schemas.report import Report, Metadata

def parse_metadata(filepath: str) -> Metadata:
    ret = {}
    pdf = PyPDF2.PdfReader(filepath)
    for p in pdf.pages:
        t = p.extract_text()

        # adresat
        match_inf = re.search(r"(\w+\s)?(\w*\s)?(\w+)\n([\w. \d\/]+)\n(\d{2}-\d{3} \w*)", t)
        if match_inf:
            (name, name2, last_name, address1, address2) = match_inf.groups()
            name = name or ""
            name = name.strip()
            name2 = name2 or ""
            name2 = name2.strip()
            ret["receiver_name"] = name.strip()
            ret["receiver_name2"] = name2.strip()
            ret["receiver_last_name"] = last_name.strip()
            ret["receiver_address"] = ",".join([address1.strip(), address2.strip()])

        match_inf = re.search(r"(\w+)\s(\w*\s)?(\w+)\s+PESEL:\s*(\d{11})", t)
        if match_inf:
            (name, name2, last_name, pesel) = match_inf.groups()
            name2 = name2 or ""
            name2 = name2.strip()
            ret["receiver_name"] = name.strip()
            ret["receiver_name2"] = name2.strip()
            ret["receiver_last_name"] = last_name.strip()
            ret["receiver_pesel"] = pesel.strip()

        # unp
        match_inf = re.search(r"UNP:\s?(\d{6}-\d\d-\d{6})", t)
        if match_inf:
            (unp,) = match_inf.groups()
            ret["unp"] = unp.strip()

        # znak sprawy
        match_inf = re.search(r"Znak sprawy:\s?(.*)\n", t)
        if match_inf:
            (zs,) = match_inf.groups()
            ret["znak_sprawy"] = zs.strip()

        # tytul sprawy
        match_inf = re.search(r"Sprawa:\s?([\w\s]+)\n", t)
        if match_inf:
            (ts,) = match_inf.groups()
            ret["tytul_sprawy"] = ts.strip()

        # data
        match_inf = re.search(r"(?:\w+),\s(\d?\d\s\w+\s\d{4}\sroku)", t)
        if match_inf:
            (date,) = match_inf.groups()
            ret["date"] = date.strip()

        # sender
        match_inf = re.search(r"Kontakt:\s?([\w ]+)\n.*\ntel\.?\s(\+[\d ]+)\n(.*)", t)
        if match_inf:
            (name, phone, email) = match_inf.groups()
            ret["sender_name"] = name.strip()
            ret["sender_phone"] = phone.strip()
            ret["sender_email"] = email.strip()

        # sender2
        match_inf = re.search(r"e-mail:\s?([\w.]+@[\w.]+).*ePUAP\s(\/\w+\/\w+).*(?:[\w.]+)\s([\w ]+),(.*)\n?", t)
        if match_inf:
            (email, epuap, name, address) = match_inf.groups()
            ret["sender_epuap"] = epuap.strip()
            ret["sender_name2"] = name.strip()
            ret["sender_address"] = address.strip()

        # nip
        match_inf = re.search(r"NIP:?\s?(\d{3}-\d{3}-\d{2}-\d{2})", t)
        if match_inf:
            (nip,) = match_inf.groups()
            ret["nip"] = nip.strip()

    return Metadata(**ret)
