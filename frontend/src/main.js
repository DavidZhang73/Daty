import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueLS from 'vue-ls'

let options = {
    namespace: 'vuejs__',
    name: 'ls',
    storage: 'local',
};

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false;

Vue.use(ElementUI);
Vue.use(VueLS, options);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
