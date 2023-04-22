import {useRef} from 'react'

const Chat = ({chatSocket, messages}) => {
    const input = useRef()
    const handlePressEnter = (event) => {
        if (event.key === 'Enter') {
            chatSocket.send(JSON.stringify({
                data: event.target.value,
                action: 'send_message',
                request_id: new Date().getTime()
            }))
            event.target.value = ''
        }

    }

    return (
        <div>
            <div>
                {messages.map(message => <div key={message.id}>
                    {message.user}: {message.message}
                </div>)}
            </div>
            <input type="text" onKeyDown={handlePressEnter} ref={input}/>
        </div>
    )
}

export {Chat}