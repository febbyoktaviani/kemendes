let base_url = ''

if(process.env.NODE_ENV === 'development') {
    base_url = 'http://localhost:5000'
} else {
    base_url = ''
}

export default base_url;