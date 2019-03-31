<template>
    <div class="center-wrap">
        <Aside></Aside>
        <div class="center">
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
        components: {
            Aside,
            CenterHeader
        }
    }
</script>

<style lang="stylus">
    .center-wrap {

        .center {
            padding 5px 0 30px 200px

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
