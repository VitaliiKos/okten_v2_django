import {useEffect, useState} from 'react'
import {autoParkService} from '../../services'
import {AutoPark} from '../AutoPark/AutoPark'
import {AutoParkForm} from '../AutoParkForm/AutoParkForm'
// import { Chat } from '../Chat/Chat'
import css from './AutoPark.module.css'
import {socketService} from '../../services/socket.service'
import {Chat} from "../Chat/Chat";

const AutoParks = () => {
    const [autoParks, setAutoParks] = useState([])
    const [chatSocket, setChatSocket] = useState(null)
    const [messages, setMessages] = useState([])

    useEffect(() => {
        autoParkService.getAll().then(value => value.data).then(value => setAutoParks(value))
    }, [])

    useEffect(() => {
        chatSocketInit().then(value => setChatSocket(value))
    }, [])

    const chatSocketInit = async () => {
        const client = await socketService.chat()

        client.onopen = () => {
            console.log('Chat socket connected')
        }
        client.onmessage = (msg) => {
            setMessages(prev => [...prev, JSON.parse(msg.data)])
        }
        return client
    }
    return (
        <div className={css.AutoPark}>
            <div>
                <AutoParkForm setAutoParks={setAutoParks}/>
                <hr/>
                <div>
                    {autoParks.map(autoPark => <AutoPark key={autoPark.id} autoPark={autoPark}/>)}
                </div>
            </div>
            <Chat chatSocket={chatSocket} messages={messages}/>
        </div>
    )
}

export {AutoParks}