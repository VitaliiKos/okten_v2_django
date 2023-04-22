import {authService} from "./auth.service";
import {w3cwebsocket as W3Websocket} from 'websocket'

const baseURL = 'ws://localhost/api/v1'

const connect = async (room) => {
    const {data: {token}} = await authService.getSocketToken();
    return new W3Websocket(`${baseURL}/auto_parks/${room}?token=${token}`)
}
const socketService = {
    chat: async () => await connect('chat'),
    autoPark: async () => await connect('auto_park')
}
export {socketService}