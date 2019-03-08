<template>
    <div class="user-password-wrap">
        <div class="user-password">
            <el-steps :active="active" finish-status="success">
                <el-step title="步骤 1"></el-step>
                <el-step title="步骤 2"></el-step>
                <el-step title="步骤 3"></el-step>
            </el-steps>

            <div class="changePassword">
                <div class="step-1">
                    <p>Step 1</p>
                    <el-input placeholder="Please input new password"
                              v-model="firstInput"
                              clearable=""></el-input>
                </div>
            </div>

            <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserPassword",
        data() {
            return {
                active: 0,
                firstInput: '',
            };
        },
        methods: {
            next() {
                if (this.active++ > 2) this.active = 0;
            }
        }
    }
</script>

<style lang="stylus">
    .user-password-wrap {
        height 100%
        width 100%

        .user-password {
            margin 0 auto
            width 70%
        }
    }
</style>
