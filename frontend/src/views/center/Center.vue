<template>
    <div class="center-wrap">
        <Aside></Aside>
        <div class="center" :style="centerPadding">
            <CenterHeader class="centerHeader"></CenterHeader>
            <div class="form">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
    import Aside from '../../components/center/Aside'
    import CenterHeader from '../../components/center/CenterHeader'

    export default {
        name: "center",
        data() {
            return {
                centerPadding: 'padding-left: 200px;'
            }
        },
        components: {
            Aside,
            CenterHeader
        }
    }
</script>

<style lang="stylus">
    .center-wrap {

        .center {
            padding-top 5px
            padding-right 0
            padding-bottom 30px

            .centerHeader {
                margin-top 60px
            }

            .form {
                margin 10px 20px 20px 20px
                padding 20px
                background-color #fff
                border-radius 5px
                border solid 1px #e6e6e6
            }
        }
    }
</style>
