import React from 'react';
import {Card} from 'antd';
import axios from 'axios';

class ArticleDetail extends React.Component {
    state = {
        article: []    
    }

    componentDidMount() {
        const articleId = this.props.match.params.articleId;
        axios.get(`http://127.0.0.1:8000/api/movie/article/${articleId}`)
            .then(res => {
                this.setState({
                    article: res.data
                });
                console.log(res);
            })
    }

    render() {
        return (
            <Card title={this.state.article.title}>
                <p>{this.state.article.content}</p>
            </Card>
        )
    }
}

export default ArticleDetail;