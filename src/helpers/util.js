import { base_url } from '@/store/config';

const getImageUrl = function(filepath) {
    const image_url = base_url + filepath
    return image_url
}

export { getImageUrl }