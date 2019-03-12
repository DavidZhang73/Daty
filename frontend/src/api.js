import {Message} from 'element-ui';
import router from './router'

export default {
    login(email, password) {
        return fetchAPI('/api/user/login/', 'post', {
            email,
            password
        })
    },
    logout() {
        return fetchAPI('/api/user/logout/', 'get')
    },
    checkEmail(email) {
        return fetchAPI('/api/user/checkEmail/', 'post', {
            email
        })
    },
    signin(email, username, phone, qq, password) {
        return fetchAPI('/api/user/signin/', 'post', {
            email,
            username,
            phone,
            qq,
            password
        })
    },
    forgetPassword(email) {
        return fetchAPI('/api/user/forgetPassword/', 'post', {
            email
        })
    },
    forgetPasswordReset(uuid, password) {
        return fetchAPI('/api/user/forgetPasswordReset/', 'post', {
            uuid,
            password
        })
    }
}

/**
 * 封装fetch
 * @param url api url
 * @param method get/post/put/delete
 * @param data data to be json
 * @param params urlencoded
 * @returns {Promise<Response>}
 */
function fetchAPI(url, method, data = null, params = null) {
    let body = null;
    let headers = {
        'Content-Type': 'application/json'
    };
    if (data) {
        body = JSON.stringify(data);
    } else if (params) {
        url += '?' + (new URLSearchParams(params)).toString();
    }
    return fetch(url, {
        headers: headers,
        method: method,
        body: body,
    }).then(res => {
        if (res.status === 401) {
            throw (new Error(res.status))
        } else if (res.status === 403) {
            Message.error({duration: 5000, showClose: true, message: '用户未登录'});
            router.push({name: 'login'})
        }
        return res.json()
    }).catch(e => {
        console.log('fetchAPI function ERROR: ' + e);
        Message.error({duration: 0, showClose: true, message: e})
    })
}
