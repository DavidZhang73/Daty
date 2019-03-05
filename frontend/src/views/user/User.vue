<template>
	<div class="user-wrap">
		<Background
			img-name="user_background.jpg"
			:blur="true"></Background>
		<router-view></router-view>
	</div>
</template>

<script>
    import Background from '../../components/Background'

    export default {
        name: "User",
        components: {
            Background
        }
    }
</script>

<style lang="stylus">
	.user-wrap {
		height 100%
		width 100%
	}
</style>
