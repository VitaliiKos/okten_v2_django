import { axiosService } from './axios.service'
import { urls } from '../constants'

const autoParkService = {
  getAll:()=>axiosService.get(urls.autoParks),
  create:(autoPark)=>axiosService.post(urls.autoParks, autoPark)
}

export {
  autoParkService
}
