<template>
    <div class="addNewCollection-wrap">
        <el-row>
            <el-col class="steps"
                    :lg="{span: 24}"
                    :sm="{span: 24}"
                    :xs="{span: 24}">
                <el-steps :active="active" align-center>
                    <el-step title="步骤1" description="这是一段很长很长很长的描述性文字"></el-step>
                    <el-step title="步骤2" description="这是一段很长很长很长的描述性文字"></el-step>
                    <el-step title="步骤3" description="这是一段很长很长很长的描述性文字"></el-step>
                </el-steps>
            </el-col>
            <!--<div class="block">-->
            <!--<span class="demonstration">起始日期时刻为 12:00:00，结束日期时刻为 08:00:00</span>-->
            <!--<el-date-picker-->
            <!--v-model="value2"-->
            <!--type="datetimerange"-->
            <!--align="right"-->
            <!--value-format="yyyy-MM-dd hh:mm:ss"-->
            <!--start-placeholder="开始日期"-->
            <!--end-placeholder="结束日期"-->
            <!--:default-time="['12:00:00', '08:00:00']">-->
            <!--</el-date-picker>-->
            <!--</div>-->
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "AddNewCollection",
        data() {
            return {
                active: 0,
                collectionForm: {
                    name: '',
                },
            }
        },
        watch: {},
        methods: {}
    }
</script>

<style lang="stylus">
    .addNewCollection-wrap {

    }
</style>