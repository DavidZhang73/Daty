<template>
    <el-row class="editUserGroup-wrap"
            v-loading="Loading"
            element-loading-text="拼命加载中"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(0, 0, 0, 0.8)">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:18}">
        </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "EditUserGroup",
        data() {
            return {
                Loading: true,
                userGroupForm: {},
            }
        },
        mounted() {


            console.log(this.$route.params);
            //TODO
        }
    }
</script>

<style lang="stylus">

</style>