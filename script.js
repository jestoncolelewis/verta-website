function retrieve(id) {
    const input = document.getElementById(id)
    let usremail = input.value
    const data = {email: usremail}

    fetch(
        'https://0cxjlr27zj.execute-api.us-west-2.amazonaws.com/items',
        {method: 'POST',
        header: {
            'Content-Type': 'applications/json'
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data );
    })
    .catch((error) => {
        console.log('Error:', error);
    })
}