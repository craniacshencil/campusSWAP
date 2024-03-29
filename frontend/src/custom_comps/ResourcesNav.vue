<template >
    <div class="resource-nav-wrapper h-8rem flex w-11 gap-3">
       <div ref = "findResource" class="find-resource-redirect-wrapper flex-1 flex flex-column h-full text-5xl pt-3 pl-3 border-round-md currently-active" @click = "displayFindResources">
            <span>Find Resources</span>
            <icon class = "pi pi-arrow-right text-4xl font-bold align-self-end pr-5 pb-5" />
        </div>
        <div ref = "createResource" class="create-resource-redirect-wrapper flex-1 flex flex-column h-full text-5xl pt-3 pl-3 border-round-md" @click = "displayCreateResources">
            <span>Create Resources</span>
            <icon class = "pi pi-arrow-right text-4xl font-bold align-self-end pr-5 pb-5" />
        </div> 
    </div>
</template>

<script>
export default{
    name: "ResourcesNav",
    methods: {
        displayFindResources(){
            let classList = this.$refs.findResource.classList
            classList= Array.from(classList)
            if(!classList.includes("currently-active")){
                    this.$refs.findResource.classList.add("currently-active")
                    this.$refs.createResource.classList.remove("currently-active")
                    this.$emit('sendDisplayInfo', 'find resources')
            }
        },

        displayCreateResources(){
            let classList = this.$refs.createResource.classList
            classList= Array.from(classList)
            if(!classList.includes("currently-active")){
                this.$refs.createResource.classList.add("currently-active")
                this.$refs.findResource.classList.remove("currently-active")
                this.$emit('sendDisplayInfo', 'create resources')
            }
        },
    }
}
</script>


<style scoped>
.create-resource-redirect-wrapper,
.find-resource-redirect-wrapper{
    background-color: rgb(50, 50, 50)
}

.create-resource-redirect-wrapper:hover span,
.find-resource-redirect-wrapper:hover span,
.currently-active span{
    transition: all ease-in-out 300ms;
    transform: translateX(.5rem);
    color: black;
}

.create-resource-redirect-wrapper:hover icon,
.find-resource-redirect-wrapper:hover icon,
.currently-active icon{
    transition: all ease-in-out 300ms;
    transform: translateX(.8rem) scale(1.2);
    color: black;
    font-weight: 900;
}

.create-resource-redirect-wrapper:hover,
.find-resource-redirect-wrapper:hover, 
.currently-active{
    transition: all ease-in-out 300ms;
    cursor: pointer;
    background: #22d3ee;
    color: black;
    -webkit-box-shadow: 10px 10px 60px -10px rgba(34,211,238,1);
    -moz-box-shadow: 10px 10px 60px -10px rgba(34,211,238,1);
    box-shadow: 10px 10px 60px -10px rgba(34,211,238,1);
}
</style>