<template>
<div class="pure-g">
    <div v-for="item in Grid" class="pure-u-1-5">
        <div class="padded">
            <div class="image" :style="'background-image: url(' + item.imgHref + ')'">
                <a :href="item.currentUrl"><img :src="placeholder" class="pure-img"></a>
            </div>
        </div>
    </div>
</div>
</template>

<script src="./grid.js"></script>

<style scoped>
    .padded {
        padding: 1px;
    }

    .image {
        background-position-x: 50%;
        background-position-y: 50%;
        background-repeat: no-repeat;
        background-size: cover;
    }
</style>
