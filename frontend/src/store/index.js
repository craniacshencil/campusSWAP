// store/index.js
import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { userStore } from './modules/userModule'

const userState = createPersistedState({
    storage: window.sessionStorage,
    key: "user",
    paths: ["userStore.user"]
})
const authState = createPersistedState({
    storage: window.sessionStorage,
    key: "isAuthenticated",
    paths: ["userStore.isAuthenticated"]
})
export const store = createStore({
  modules: {
    userStore,
  },
  plugins: [ userState, authState ]
})
