let base_url = ''

if (process.env.NODE_ENV === 'development') {
  base_url = 'http://localhost:5000'
} else {
  base_url = ''
}

export default {
  base_url,
  staticToken:
    'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzY0NzczMjEsImlkZW50aXR5IjoiYWRtaW4iLCJpYXQiOjE1NDQ5NDEzMjEsImp0aSI6ImQzNTkyODQ0LWY4ODItNDNiMS1hMDcwLWQ2NzdlNGViZjdhMiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU0NDk0MTMyMX0.9zqJWoO7Fq9QOCzpvySDsLnGOVSlcwc4DxLR1s2wfLY'
}
