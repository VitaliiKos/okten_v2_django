const baseURL = 'api/v1'
const auth = '/auth'

const urls = {
  autoParks: '/auto_parks',
  auth: {
    login: auth,
    socket: `${auth}/socket`
  }
}

export {
  baseURL,
  urls
}