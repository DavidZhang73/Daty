<template>
    <div class="user-password-wrap">
        <div class="user-password">
            <el-steps :active="active" finish-status="success">
                <el-step title="步骤 1"></el-step>
                <el-step title="步骤 2"></el-step>
                <el-step title="步骤 3"></el-step>
            </el-steps>

            <div class="changePassword">
                <div class="step-1" v-if="stepOneSeen">
                    <el-input type="password"
                              v-model="oldPassword"
                              clearable>
                        <template slot="prepend">请输入旧的密码</template>
                    </el-input>
                </div>
                <div class="step-2" v-if="stepTwoSeen">
                    <el-input type="text"
                              placeholder="密码不能全为数字且应大于8位"
                              v-model="firstInput"
                              clearable>
                        <template slot="prepend">请输入新的密码</template>
                    </el-input>
                </div>
                <div class="step-3" v-if="stepThreeSeen">
                    <el-input type="text"
                              placeholder="密码不能全为数字且应大于8位"
                              v-model="secondInput"
                              clearable>
                        <template slot="prepend">请再次输入新的密码</template>
                    </el-input>
                </div>
            </div>
            <el-button class="submitChange" v-if="submitBtn" type="success" @click="submitData" plain>
                提交
            </el-button>
            <el-button-group v-if="btnGroup">
                <el-button
                        type="primary"
                        icon="el-icon-arrow-left"
                        @click="last"
                        :disabled="canSeenLastBtn">上一步
                </el-button>
                <el-button
                        type="primary"
                        @click="next"
                        :disabled="canSeenNextBtn">下一步<i
                        class="el-icon-arrow-right el-icon--right"></i>
                </el-button>
            </el-button-group>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserPassword",
        data() {
            return {
                active: 0,
                oldPassword: '',
                firstInput: '',
                secondInput: '',
                canSeenLastBtn: true,
                canSeenNextBtn: false,
                stepOneSeen: true,
                stepTwoSeen: false,
                stepThreeSeen: false,
                submitBtn: false,
                btnGroup: true,
            };
        },
        methods: {
            next() {
                this.active++;
            },
            last() {
                this.active--;
            },
            submitData() {

            },
        },
        watch: {
            active(newVal) {
                console.log('watch: ' + newVal);
                if (newVal === 1) {
                    this.canSeenNextBtn = false;
                    this.canSeenLastBtn = false;

                    this.stepOneSeen = false;
                    this.stepTwoSeen = true;
                    this.stepThreeSeen = false;

                    this.submitBtn = false;
                    this.btnGroup = true;
                } else if (newVal === 2) {
                    this.canSeenNextBtn = false;
                    this.canSeenLastBtn = false;

                    this.stepOneSeen = false;
                    this.stepTwoSeen = false;
                    this.stepThreeSeen = true;

                    this.submitBtn = false;
                    this.btnGroup = true;
                } else if (newVal === 3) {
                    this.canSeenNextBtn = true;
                    this.canSeenLastBtn = false;
                    this.stepOneSeen = false;
                    this.stepTwoSeen = false;
                    this.stepThreeSeen = false;

                    this.submitBtn = true;
                    this.btnGroup = false;
                } else if (newVal === 0) {
                    this.canSeenNextBtn = false;
                    this.canSeenLastBtn = true;

                    this.stepOneSeen = true;
                    this.stepTwoSeen = false;
                    this.stepThreeSeen = false;

                    this.submitBtn = false;
                    this.btnGroup = true;
                } else {
                    this.canSeenNextBtn = false;
                    this.canSeenLastBtn = false;

                    this.stepOneSeen = true;
                    this.stepTwoSeen = false;
                    this.stepThreeSeen = false;

                    this.submitBtn = false;
                    this.btnGroup = true;
                }
            }
        }
    }
</script>

<style lang="stylus">
    .user-password-wrap {
        margin-top 50px
        height 100%
        width 100%

        .user-password {
            margin 0 auto
            width 70%

            .changePassword {
                margin-top 40px

                .step-1 {
                    width 70%
                }

                .step-2 {
                    width 70%
                }

                .step-3 {
                    width 70%
                }
            }

            .el-button-group {
                margin-top 30px
            }
        }
    }
</style>
