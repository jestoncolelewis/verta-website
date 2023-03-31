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
        alert('Successfully submitted, we\'ll be in touch!');
    })
    .catch((error) => {
        alert('Please try again.');
    })
}