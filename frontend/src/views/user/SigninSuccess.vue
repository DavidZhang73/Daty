<template>
	<div class="signin-success-wrap">
		<RedirectMessage message="注册成功！"
		                 jump_to_name="登陆页面"
		                 jump_to_path="/user/login"></RedirectMessage>
	</div>
</template>

<script>
    import RedirectMessage from '../../components/RedirectMessage'

    export default {
        name: "SigninSuccess",
        components: {
            RedirectMessage
        }
    }
</script>

<style lang="stylus">
</style>
