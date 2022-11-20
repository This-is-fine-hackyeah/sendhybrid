import axios from 'axios';

const apiUrl = 'http://localhost'
export const api = {
  async sendFiles(files) {
    for(const file of files) {
      console.log('test')

      const formData = new FormData();
      formData.append("photo", file);

      //await axios.post(`${apiUrl}/api/v1/login/access-token`, formData);
    }
  }
};
