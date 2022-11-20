import axios from 'axios';

axios.defaults.headers.common = {'Authorization': `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Njk2MjcyNjYsInN1YiI6IjEifQ.r2IirUjhS3d64RXF31kVVdZJI1TwvDeiAy0JEcy-f6o`}

const apiUrl = 'http://localhost'
export const api = {
  async sendFiles(files) {
    for(const file of files) {
      const formData = new FormData();
      formData.append("file", file);

      await axios.post(`${apiUrl}/api/v1/documents/upload`, formData);
    }
  },

  async sendFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    const resp = await axios.post(`${apiUrl}/api/v1/documents/upload`, formData);
    return resp.data.id
  },

  async checkStatusForDocument(id: string) {
    const resp = await axios.get(`${apiUrl}/api/v1/documents/${id}/report`);
    return resp.data
  }
};
