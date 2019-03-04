<template>
	<div class="forget-password-wrap">
		<router-link :to="{name: 'forgetpassword.step1'}">Step1</router-link>
		|
		<router-link :to="{name: 'forgetpassword.step2'}">Step2</router-link>
		<router-view></router-view>
	</div>
</template>

<script>
    export default {
        name: "ForgetPassword"
    }
</script>

<style lang="stylus">
	.forget-password-wrap {
		padding-top 60px
	}
</style>
