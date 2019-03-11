import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: null
    },
    getters: {
        isLogin(state) {
            return !!state.user;
        }
    },
    mutations: {
        userMutation(state, user) {
            state.user = user;
        }
    },
    actions: {
        userLogin(context, user) {
            Vue.ls.set('user', JSON.stringify(user));
            context.commit('userMutation', user);
        },
        userLogout(context) {
            Vue.ls.set('user', null);
            context.commit('userMutation', null)
        }
    }
})
