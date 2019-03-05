import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home'
import About from './views/About'

import User from './views/user/User'
import Login from './views/user/Login'
import Signin from './views/user/Signin'

import ForgetPassword from './views/user/ForgetPassword'
import ForgetPasswordReset from "./views/user/ForgetPasswordReset"

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
            path: '/user',
            component: User,
            children: [
                {
                    path: 'login',
                    name: 'login',
                    component: Login,
                },
                {
                    path: 'signin',
                    name: 'signin',
                    component: Signin
                },
                {
                    path: 'forgetPassword',
                    name: 'forgetPassword',
                    component: ForgetPassword,
                },
                {
                    path: 'forgetPassword/reset/:uuid',
                    name: 'forgetPasswordReset',
                    component: ForgetPasswordReset,
                },
            ]
        },
        {
            path: '*',
            name: 'notfound',
            component: NotFound
        }

    ]
})
