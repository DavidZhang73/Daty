<template>
    <div class="notfound-wrap">
        <div class="notfound">
            404 Not Found
        </div>
    </div>
</template>

<script>
    export default {
        name: "NotFound",
        data() {
            return {
                returnToHome: false,
                autoTime: 10
            }
        },
        mounted() {
            this.NotFoundTimer();
        },
        methods: {
            NotFoundTimer() {
                var timer = setInterval(() => {
                    this.autoTime--;
                    if (this.autoTime <= 0) {
                        this.returnToHome = true;
                        clearInterval(timer);
                    }
                }, 1000)
            }
        },
        watch: {
            returnToHome: function (newVal) {
                if (newVal === true) {
                    this.$router.push({name: 'home'})
                }
            }
        }
    }
</script>

<style lang="stylus">
    .notfound-wrap {
        width 100%
        height 100%

        .notfound {
            position absolute
            top 50%
            left 50%
            transform translate(-50%, -50%)
            width 400px
            height 400px
            border 1px solid black
        }
    }
</style>
