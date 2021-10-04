const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/logs/'
    + 'sms-logs'
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// const message = messageInputDom.value;
// chatSocket.send(JSON.stringify({
//     'message': message
// }));