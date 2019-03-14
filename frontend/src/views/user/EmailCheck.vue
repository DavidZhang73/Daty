<template>
	<div class="signin-email-check-wrap">
		<RedirectMessage message="已发送验证邮件到邮箱，请在邮箱中继续操作"
		                 jump_to_name="主页"
		                 jump_to_path="/"></RedirectMessage>
	</div>
</template>

<script>
    import RedirectMessage from '../../components/RedirectMessage'

    export default {
        name: "EmailCheck",
        components: {
            RedirectMessage
        }
    }
</script>

<style lang="stylus">

</style>
