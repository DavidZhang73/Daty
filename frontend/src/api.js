import {Message} from 'element-ui';

export default {
    login(email, password) {
        return fetchAPI('/api/user/login', 'post', {
            email,
            password
        })
    },
    logout() {
        return fetchAPI('/api/user/logout', 'get')
    },
    signinEmailCheck(email) {
        return fetchAPI('/api/user/signin/emailCheck', 'post', {
            email
        })
    },
    signin(email, username, phone, qq, password) {
        return fetchAPI('/api/user/signin', 'post', {
            email,
            username,
            phone,
            qq,
            password
        })
    },
    forgetPasswordEmailCheck(email) {
        return fetchAPI('/api/user/forgetPassword/emailCheck', 'post', {
            email
        })
    },
    forgetPassword(email) {
        return fetchAPI('/api/user/forgetPassword', 'post', {
            email
        })
    },
    forgetPasswordReset(uuid, password) {
        return fetchAPI('/api/user/forgetPassword/reset', 'post', {
            uuid,
            password
        })
    },
    //Center
    //center.useInfo
    userInfoNameChange() {

    },
    userInfoPhoneNumberChange() {

    },
    userInfoQQChange() {

    },
    //Center.userPassword
    checkOldPassword(email, oldPassword) {

    },
    changePassword(email, newPassword) {

    },
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
    let content_type = '';
    if (data && params) {
        throw (new Error('不能同时使用data和params'))
    } else if (data) {
        body = JSON.stringify(data);
        content_type = 'application/json'
    } else if (params) {
        body = params;
        content_type = 'x-www-form-urlencoded'
    }
    return fetch(url, {
        headers: {
            'content-type': content_type,
        },
        method: method,
        body: body,
    }).then(res => {
        if (res.status === 401 || res.status === 403) {
            throw (new Error(res.status))
        }
        return res.json()
    }).catch(e => {
        console.log('fetchAPI function ERROR: ' + e);
        Message.error({duration: 0, showClose: true, message: e})
    })
}
