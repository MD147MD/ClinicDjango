const container = document.getElementById("log-container")

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/logs/'
    + 'sms-logs'
    + '/'
);

all = []

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if(data["type"] && data["type"] == "append"){
        console.log(data["data"][0]);
        add_data(data["data"][0])
    }
    if(data["type"] && data["type"] == "edit"){
        id = data["data"][0]["pk"]
        document.getElementById(id).innerHTML = get_data(data["data"][0])
        all = all.filter(x=>x.pk != id)
        all.push(data["data"][0])
    } else {
        all = data
        // for(let attempt of data){
        //     add_data(attempt)
        // }
        show()
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

function show(){
    for(let attempt of all){
        add_data(attempt)
    }
}

function add_data(data){
    let result = get_data(data)
    container.innerHTML += `
    <tr id="${data["pk"]}">
        ${result}
    </tr>
    ` 
}

function get_data(data){
    let id = data["fields"]["pk"]
    let code = data["fields"]["code"]
    let created_at = data["fields"]["created_at"]
    let ip = data["fields"]["ip"]
    let used = data["fields"]["used"]
    let phone_number = data["fields"]["user"][0]
    return `        
            <td>${phone_number}</td>
            <td>${code}</td>
            <td>${ip}</td>
            <td>${get_used(used)}</td>
            <td>${get_date(created_at)}</td>
    `
}


function get_date(data){
    let date = new Date(data).toLocaleDateString('fa-ir', { year: 'numeric', month: '2-digit', day: '2-digit',hour:"2-digit",minute:"2-digit"})
    return date
}

function get_used(used){
    if(used){
    return `<p class="text-success">
        <i class="fa fa-check-square" aria-hidden="true"></i>
    </p>`
    } else {
        return `<p class="text-danger">
            <i class="fa fa-window-close" aria-hidden="true"></i>
        </p>`
    }        
}

// const message = messageInputDom.value;
// chatSocket.send(JSON.stringify({
//     'message': message
// }));