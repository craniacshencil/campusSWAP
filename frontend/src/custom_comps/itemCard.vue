<template>
    <Card style="width: 25rem; overflow: hidden">
    <template #header>
        <img alt="user header" src="" />
    </template>
    <template #title>Advanced Card</template>
    <template #subtitle>Card subtitle</template>
    <template #content>
        <p class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque
            quas!
        </p>
    </template>
    <template #footer>
        <div class="flex gap-3 mt-1">
            <Button label="Cancel" severity="secondary" outlined class="w-full" />
            <Button label="Save" class="w-full" />
        </div>
    </template>
</Card>
</template>

<script>
import Button from 'primevue/button'
import Card from 'primevue/card'
    export default{
        name: "itemCard",
        components: { Card, Button }
    }
</script>
