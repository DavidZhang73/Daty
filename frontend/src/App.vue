<template>
	<div id="app">
		<Header></Header>
		<router-view/>
		<Footer></Footer>
	</div>
</template>

<script>
    import Header from './components/Header'
    import Footer from './components/Footer'

    export default {
        name: 'App',
        components: {
            Header,
            Footer
        },
        methods: {},
        created() {
            if (document.cookie.search('sessionid') === -1) {
                this.$store.dispatch('userLogout')
            } else {
                if (!this.$store.state.user) {
                    let user_info_ls = JSON.parse(this.$ls.get('user'));
                    if (user_info_ls) {
                        this.$store.commit('userMutation', user_info_ls);
                    }
                }
            }
        }
    }
</script>

<style>
	html, body {
		height: 100%;
		background-color: #f9fafe;
		font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
	}

	body, h1, h2, h3, h4, h5, h6, hr, p, blockquote, dl, dt, dd, ul, ol, li, pre, form, fieldset, legend, button, input, textarea, th, td {
		margin: 0;
		padding: 0;
	}

	h1 {
		font-size: 20px;
	}

	h2 {
		font-size: 18px;
	}

	h3 {
		font-size: 16px;
	}

	h4 {
		font-size: 14px;
	}

	h5 {
		font-size: 13px;
	}

	h6 {
		font-size: 12px;
	}

	body, button, input, select, textarea {
		font-size: 16px;
	}

	address, cite, dfn, em, var {
		font-style: normal;
	}

	code, kbd, pre, samp {
		font-family: Helvetica Neue, couriernew, courier, monospace;
	}

	small {
		font-size: 12px;
	}

	ul, ol {
		list-style: none;
	}

	a {
		color: #404040;
		text-decoration: none;
	}

	sup {
		vertical-align: text-top;
	}

	sub {
		vertical-align: text-bottom;
	}

	legend {
		color: #000;
	}

	fieldset, img {
		border: 0;
	}

	button, input, select, textarea {
		font-size: 100%;
	}

	[v-cloak] {
		display: none;
	}

	#app {
		height: 100%;
	}
</style>
