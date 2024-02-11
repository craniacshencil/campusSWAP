import './assets/style.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import 'primevue/resources/primevue.min.css';
import 'primeflex/primeflex.css'
import 'primevue/resources/themes/aura-dark-cyan/theme.css'
import 'primeicons/primeicons.css'

import Home from "./pages/Home.vue"
import Login from "./pages/Login.vue"
import Register from "./pages/Register.vue"
import Test from "./pages/test.vue"
import Buy from "./pages/Buy.vue"
import Wishlist from "./pages/Wishlist.vue"
import Sell from "./pages/Sell.vue"

const routes = [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/test', component: Test },
    { path: '/buy', component: Buy },
    { path: '/wishlist', component: Wishlist},
    { path: '/sell', component: Sell },

]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)
app.use(router)
app.use(PrimeVue, { ripple: true})

app.mount('#app')
