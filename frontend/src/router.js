import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home'
import About from './views/About'
import Login from './views/Login'
import Signin from './views/Signin'

import ForgetPassword from './views/FogetPassword/ForgetPassword'
import ForgetPasswordStep1 from './views/FogetPassword/Step1'
import ForgetPasswordStep2 from './views/FogetPassword/Step2'

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
            path: '/forget-password',
            component: ForgetPassword,
            children: [
                {
                    path: "",
                    name: 'forget-password-step1',
                    component: ForgetPasswordStep1
                },
                {
                    path: "/step2",
                    name: 'forget-password-step2',
                    component: ForgetPasswordStep2
                }
            ]
        },
        {
            path: '*',
            name: 'notfound',
            component: NotFound
        }

    ]
})
