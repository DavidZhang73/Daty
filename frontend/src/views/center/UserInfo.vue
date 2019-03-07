<template>
    <div class="user-info-wrap">
        <el-collapse v-model="activeNames" @change="handleChange">
            <el-collapse-item title="修改姓名" name="1">
                <el-form :inline="true"
                         class="formItem"
                         :model="ruleFormName"
                         :rules="rulesName"
                         ref="ruleFormName">
                    <el-form-item label="新的姓名" prop="name">
                        <el-input
                                v-model.trim="ruleFormName.name"
                                placeholder="张某某"
                                auto-complete="name"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmitName">提交</el-button>
                    </el-form-item>
                </el-form>
            </el-collapse-item>
            <el-collapse-item title="修改手机号" name="2">
                <el-form :inline="true"
                         class="formItem"
                         :model="ruleFormPhonenumber"
                         :rules="rulesPhonenumber"
                         ref="ruleFormPhonenumber">
                    <el-form-item label="新的手机号" prop="phoneNumber">
                        <el-input
                                v-model.trim="ruleFormPhonenumber.phoneNumber"
                                placeholder="13088888888"
                                auto-complete="phoneNumber"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmitPhonenumber">提交</el-button>
                    </el-form-item>
                </el-form>
            </el-collapse-item>
            <el-collapse-item title="效率 Efficiency" name="3">
                <div>简化流程：设计简洁直观的操作流程；</div>
                <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
                <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
            </el-collapse-item>
            <el-collapse-item title="可控 Controllability" name="4">
                <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
                <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>

<script>
    export default {
        name: "UserInfo",
        data() {
            var validateName = (rule, value, callback) => {
                //必填。150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。
                if (!value) {
                    return callback(new Error('请输入姓名'))
                } else if (value.length > 150) {
                    return callback(new Error('姓名应该小于150个字符'))
                }
                return callback()
            };
            var validatePhone = (rule, value, callback) => {
                let phoneRex = /^1[34578]\d{9}$/;
                if (!value) {
                    return callback()
                } else if (!phoneRex.test(value)) {
                    return callback(new Error('手机号格式不正确'))
                }
                return callback()
            };
            return {
                activeNames: ['1'],
                ruleFormName: {
                    name: ''
                },
                ruleFormPhonenumber: {
                    phoneNumber: ''
                },
                rulesName: {
                    name: [
                        {validator: validateName, trigger: 'blur'}
                    ],
                },
                rulesPhonenumber: {
                    phoneNumber: [
                        {validator: validatePhone, trigger: 'blur'}
                    ]
                }
            }
        },
        methods: {
            handleChange(val) {
                console.log(val);
            },
            onSubmitName() {

            },
            onSubmitPhonenumber() {

            }
        }
    }
</script>

<style lang="stylus">
    .user-info-wrap {

    }
</style>
