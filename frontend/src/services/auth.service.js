import { axiosService } from './axios.service'
import { urls } from '../constants'

const authService = {
  login: async (user) => {
    const res = await axiosService.post(urls.auth.login, user)
    if (res.status === 200) {
      localStorage.setItem('access', res.data.access)
    }
    return res
  },
  getSocketToken: ()=>axiosService.get(urls.auth.socket)
}

export {
  authService
}