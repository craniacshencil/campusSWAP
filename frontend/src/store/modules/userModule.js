export const userStore = {
    state(){
        return{
            isAuthenticated: false,
            user: null,
        }
    },
    mutations: {
        toggleIsAuthenticated(state, newAuthVal){
            state.isAuthenticated = newAuthVal 
        },
        
        assignUser(state, newUser){
            state.user = newUser
        },
    }
} 