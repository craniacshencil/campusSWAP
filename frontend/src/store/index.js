// store/index.js
import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { userStore } from './modules/userModule'

const userState = createPersistedState({
    storage: window.sessionStorage,
    paths: ['userStore.isAuthenticated', 'userStore.user']
})
export default createStore({
  modules: {
    userStore,
  },
  plugins: [ userState ]
})
