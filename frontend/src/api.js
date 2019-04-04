import {Message} from 'element-ui';
import router from './router'
import 'whatwg-fetch'

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

    },
    //Center
    //center.useInfo
    updateUserInfo(username, phone, qq) {
        return fetchAPI('/api/user/', 'post', {
            username,
            phone,
            qq
        })
    },
    getUserInfo() {
        return fetchAPI('/api/user/', 'get')
    },

    //Center.userPassword
    resetUserPassword(new_password) {
        return fetchAPI('/api/user/changePassword/', 'post', {
            new_password
        })
    },

    //Center.GroupList
    getUserGroupType() {
        return fetchAPI('/api/usergroup/type/', 'get')
    },

    getUserGroup(params) {
        return fetchAPI('/api/usergroup/', 'get', null, params)
    },

    updateUserGroup(name, type, users) {
        return fetchAPI('/api/usergroup/', 'post', {
            name,
            type,
            users
        })
    },

    getUserGroupById(params, id) {
        return fetchAPI('/api/usergroup/' + id + '/', 'get', null, params)
    }
}


/**
 * 获得cookie对应键的值
 * @param name
 * @returns {*}
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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
    // csrf
    let headers = {
        'Content-Type': 'application/json'
    };
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(method.toUpperCase())) {
        headers['X-CSRFToken'] = getCookie('csrftoken')
    }
    if (data) {
        body = JSON.stringify(data);
    }
    if (params) {
        url += '?' + (new URLSearchParams(params)).toString();
    }
    return fetch(url, {
        credentials: 'include',
        headers: headers,
        method: method,
        body: body,
    }).then(res => {
        if (res.status === 403 || res.status === 401) {
            Message.error({duration: 5000, showClose: true, message: '用户未登录'});
            router.push({name: 'login'});
            // throw (new Error(res.status))
        } else {
            return res.json()
        }
    }).catch(e => {
        console.log('fetchAPI function ERROR: ' + e);
        Message.error({duration: 0, showClose: true, message: e})
    })
}
