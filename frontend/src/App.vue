<template>
    <div id="app">
        <Header></Header>

        <div id="nav">
            <router-link to="/">Home</router-link>
            |
            <router-link to="/about">About</router-link>
        </div>
        <router-view/>
    </div>
</template>

<script>
    import Header from '@/components/Header.vue'

    export default {
        name: 'App',
        components: {
            Header
        }
    }
</script>

<style>
    html, body {
        height: 100%;
        background-color: #f4f4f4;
    }

    body, h1, h2, h3, h4, h5, h6, hr, p, blockquote, dl, dt, dd, ul, ol, li, pre, form, fieldset, legend, button, input, textarea, th, td {
        margin: 0;
        padding: 0;
    }

    body, button, input, select, textarea {
        font-size: 16px;
    }

    address, cite, dfn, em, var {
        font-style: normal;
    }

    code, kbd, pre, samp {
        font-family: couriernew, courier, monospace;
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
        display: none
    }
</style>
