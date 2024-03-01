<template>
    <div class="void">
        <pageHeader />
        <pageNav />
        <h2 class="custom-heading">FIND THE GEAR YOU NEED</h2>
        <main class="item-card-container">
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
        </main>
    </div>
</template>

<script>
import itemCard from '@/custom_comps/itemCard.vue'
import pageHeader from '@/custom_comps/pageHeader.vue'
import pageNav from '@/custom_comps/pageNav.vue'
export default {
    components: { itemCard , pageHeader, pageNav },
}
</script>

<style scoped>
.void {
    margin: 0;
    background-color: #09090b;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.item-card-container {
    display: flex;
    flex-wrap: wrap; 
    justify-content: space-around;
    align-items: flex-start;
    width: 100%;
    max-width: 1600px;
    padding: 30px;
}

.custom-heading {
    letter-spacing: 0.2rem;
}

</style>
