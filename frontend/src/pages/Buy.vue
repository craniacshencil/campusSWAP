<template>
    <div class="void">
        <pageHeader />
        <main>
           <itemCard /> 
        </main>
    </div>
</template>

<script>
import itemCard from '@/custom_comps/itemCard.vue'
import pageHeader from '@/custom_comps/pageHeader.vue'
export default{
    components: { itemCard , pageHeader },
}
</script>

<style scoped>
.void{
    margin: 0;
    background-color: #09090b;
    height: 100%;
    width: 100%;
    
    display: flex;
    align-items: center;
    flex-direction: column;
}
</style>