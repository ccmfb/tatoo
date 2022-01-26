from tensorflow.keras.layers import Dense, Embedding
import tensorflow as tf

class FeatureEmbedding(tf.keras.layers.Layer):
    def __init__(self, cat_emb_feature_idx, cat_emb_dim_in, cat_emb_dim_out, hidden_dim, out_dim):
        super().__init__()
        self.cat_emb_feature_idx = cat_emb_feature_idx
        self.dense_hidden = Dense(hidden_dim, activation=tf.nn.relu)
        self.dense_out = Dense(out_dim, activation=tf.nn.relu) 
        self.embedding = Embedding(cat_emb_dim_in, cat_emb_dim_out)
        
    def call(self, inputs):
        x_emb = self.embedding(inputs[..., self.cat_emb_feature_idx])
        x_inputs = tf.concat([inputs[..., :self.cat_emb_feature_idx], inputs[..., self.cat_emb_feature_idx+1:], x_emb], axis=-1)
        x_out = self.dense_out(self.dense_hidden(x_inputs))
        
        return x_out