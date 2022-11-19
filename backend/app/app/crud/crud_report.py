from app.crud.base import CRUDBase

from app.models.report import Report
from app.schemas.report import ReportUpdate
from app.schemas.report import Report as ReportS


class CRUDReport(CRUDBase[Report, ReportS, ReportUpdate]):
    ...


report = CRUDReport(Report)
