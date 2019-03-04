import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home'
import About from './views/About'
import Login from './views/Login'
import Signin from './views/Signin'

import ForgetPassword from './views/ForgetPassword'
import ForgetPasswordReset from "./views/ForgetPasswordReset"

import NotFound from './views/NotFound'

Vue.use(Router);

export default new Router({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/signin',
            name: 'signin',
            component: Signin
        },
        {
            path: '/forgetPassword',
            name: 'forgetPassword',
            component: ForgetPassword,
        },
        {
            path: '/forgetPassword/reset/:uuid',
            name: 'forgetPasswordReset',
            component: ForgetPasswordReset,
        },
        {
            path: '*',
            name: 'notfound',
            component: NotFound
        }

    ]
})
