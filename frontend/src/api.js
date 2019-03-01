export default {
    login(email, password) {
        return fetchAPI('/api/user/login', 'post', {
            email,
            password
        })
    }
}

/**
 * 封装fetch
 * @param url api url
 * @param method get/post/put/delete
 * @param data params/formData
 * @returns {Promise<Response>}
 */
function fetchAPI(url, method, data) {
    return fetch(url, {
        headers: {
            'content-type': 'application/json'
        },
        method: method,
        body: JSON.stringify(data)
    }).then(res => {
        return res.json()
    }).catch(e => {
        console.log('fetchAPI function ERROR: ' + e);
        alert(e)
    })
}
