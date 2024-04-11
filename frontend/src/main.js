import './assets/style.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import { store } from './store/index'
import { createRouter, createWebHistory } from 'vue-router'
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';
import 'primevue/resources/primevue.min.css';
import 'primeflex/primeflex.css'
import 'primevue/resources/themes/aura-dark-cyan/theme.css'
import 'primeicons/primeicons.css'

//router code
import Home from "./pages/Home.vue"
import Login from "./pages/Login.vue"
import Register from "./pages/Register.vue"
import Buy from "./pages/Buy.vue"
import Resources from "./pages/Resources.vue"
import Sell from "./pages/Sell.vue"
import Settings from "./pages/Settings.vue"
import ListingDetails from './pages/ListingDetails.vue'
import AdminDash from './pages/AdminDash.vue'
import ApproveListing from './pages/ApproveListing.vue'
import ApproveResource from './pages/ApproveResource.vue'
import BanUser from './pages/BanUser.vue'
import ResourceDetails from './pages/ResourceDetails.vue'


const routes = [
    { path: '/', component: Home, name: "Home"},
    { path: '/login', component: Login, name: "Login"},
    { path: '/register', component: Register, name: "Register"},
    { path: '/buy', component: Buy, name: "Buy", meta: {
        authenticationRequired: true
    }},
    { path: '/resources', component: Resources , name: "Resources", meta: {
        authenticationRequired: true
    } },
    { path: '/sell', component: Sell, name: "Sell", meta: {
        authenticationRequired: true
    }},
    { path: '/settings', component: Settings, name: "Settings", meta: {
        authenticationRequired: true
    }},
    { path: '/listingdetails', component: ListingDetails, name: "Listing details", meta: {
        authenticationRequired: true
    }},
    { path: '/admindash', component: AdminDash, name: "Admin Dashboard", meta: {
        authenticationRequired: true,
        adminRequired: true,
    }},
    { path: '/approvelisting', component: ApproveListing, name: "Approve Listing", meta: {
        authenticationRequired: true,
        adminRequired: true,
    }},
    { path: '/approveresource', component: ApproveResource, name: "Approve Resource", meta: {
        authenticationRequired: true,
        adminRequired: true,
    }},
    { path: '/banuser', component: BanUser , name: "Ban User", meta: {
        authenticationRequired: true,
        adminRequired: true,
    }},
    { path: '/resourcedetails/:resourceId', component: ResourceDetails, name: "Resource Details", meta: {
        authenticationRequired: true
    }},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach(async (to, from) => {
    if(to.meta.authenticationRequired){
        const isAuthenticatedString= sessionStorage.getItem('isAuthenticated')
        if(isAuthenticatedString === null){ //this state is reflected when no successful login exists in the session
            return {name: "Login"}          //and you try to open a login-restricted page because store and persisted-state is not setup
        }
        const isAuthenticatedJson = JSON.parse(isAuthenticatedString)
        if(!(isAuthenticatedJson.authState)){ //this state is reflected after one successful login in the session
            return { name: "Login" }
        }
    }
})

router.beforeEach(async (to, from) => {
    if(to.meta.adminRequired){
        const adminStatus= JSON.parse(sessionStorage.getItem('user')).user.superuser_status
        if(!(adminStatus)){ //this state is reflected after one successful login in the session
            return { name: "Home" }
        }
    }
})

const app = createApp(App)
app.use(ToastService);
app.use(ConfirmationService);
app.use(router)
app.use(store)
app.use(PrimeVue, { ripple: true })

app.mount('#app')
