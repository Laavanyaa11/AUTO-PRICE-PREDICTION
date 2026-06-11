"""
Model training and evaluation module for AUTO-PRICE-PREDICTION

This module handles:
- Model training (Linear Regression, Random Forest, XGBoost, etc.)
- Model evaluation and metrics
- Cross-validation
- Model persistence
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import warnings

warnings.filterwarnings('ignore')


class PricePredictionModel:
    """Handle model training and evaluation."""
    
    def __init__(self, random_state=42):
        self.random_state = random_state
        self.model = None
        self.models = {}
        self.best_model = None
        self.best_model_name = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
    
    def split_data(self, X, y, test_size=0.2):
        """Split data into training and testing sets."""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )
        print(f"Data split: Train={self.X_train.shape[0]}, Test={self.X_test.shape[0]}")
    
    def train_linear_regression(self):
        """Train Linear Regression model."""
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        self.models['Linear Regression'] = model
        return model
    
    def train_ridge_regression(self, alpha=1.0):
        """Train Ridge Regression model."""
        model = Ridge(alpha=alpha)
        model.fit(self.X_train, self.y_train)
        self.models['Ridge Regression'] = model
        return model
    
    def train_lasso_regression(self, alpha=1.0):
        """Train Lasso Regression model."""
        model = Lasso(alpha=alpha)
        model.fit(self.X_train, self.y_train)
        self.models['Lasso Regression'] = model
        return model
    
    def train_random_forest(self, n_estimators=100, max_depth=10):
        """Train Random Forest Regressor model."""
        model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=self.random_state,
            n_jobs=-1
        )
        model.fit(self.X_train, self.y_train)
        self.models['Random Forest'] = model
        return model
    
    def train_gradient_boosting(self, n_estimators=100, learning_rate=0.1):
        """Train Gradient Boosting Regressor model."""
        model = GradientBoostingRegressor(
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            random_state=self.random_state
        )
        model.fit(self.X_train, self.y_train)
        self.models['Gradient Boosting'] = model
        return model
    
    def evaluate_model(self, model, model_name='Model'):
        """Evaluate model on test set."""
        y_pred = model.predict(self.X_test)
        
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        metrics = {
            'Model': model_name,
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'R2 Score': r2
        }
        
        return metrics, y_pred
    
    def evaluate_all_models(self):
        """Evaluate all trained models."""
        results = []
        best_r2 = -np.inf
        
        print("\n" + "="*70)
        print("MODEL EVALUATION RESULTS")
        print("="*70)
        
        for model_name, model in self.models.items():
            metrics, _ = self.evaluate_model(model, model_name)
            results.append(metrics)
            
            print(f"\n{model_name}:")
            print(f"  RMSE: ${metrics['RMSE']:,.2f}")
            print(f"  MAE:  ${metrics['MAE']:,.2f}")
            print(f"  R2:   {metrics['R2 Score']:.4f}")
            
            if metrics['R2 Score'] > best_r2:
                best_r2 = metrics['R2 Score']
                self.best_model = model
                self.best_model_name = model_name
        
        print("\n" + "="*70)
        print(f"BEST MODEL: {self.best_model_name} (R² = {best_r2:.4f})")
        print("="*70)
        
        return pd.DataFrame(results)
    
    def cross_validate(self, model, cv=5):
        """Perform k-fold cross-validation."""
        cv_scores = cross_val_score(
            model, self.X_train, self.y_train,
            cv=cv, scoring='r2', n_jobs=-1
        )
        print(f"\nCross-Validation R² Scores: {cv_scores}")
        print(f"Mean R² Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        return cv_scores
    
    def save_model(self, filepath='models/trained_model.pkl'):
        """Save the best model to disk."""
        if self.best_model:
            joblib.dump(self.best_model, filepath)
            print(f"Model saved to {filepath}")
        else:
            print("No model trained yet.")
    
    def load_model(self, filepath='models/trained_model.pkl'):
        """Load a model from disk."""
        self.model = joblib.load(filepath)
        print(f"Model loaded from {filepath}")
        return self.model
    
    def predict(self, X):
        """Make predictions using the best model."""
        if self.best_model:
            return self.best_model.predict(X)
        else:
            print("No model trained yet.")
            return None
    
    def get_feature_importance(self, feature_names=None):
        """Get feature importance from tree-based models."""
        if hasattr(self.best_model, 'feature_importances_'):
            importances = self.best_model.feature_importances_
            
            if feature_names:
                importance_df = pd.DataFrame({
                    'Feature': feature_names,
                    'Importance': importances
                }).sort_values('Importance', ascending=False)
            else:
                importance_df = pd.DataFrame({
                    'Importance': importances
                }).sort_values('Importance', ascending=False)
            
            return importance_df
        else:
            print("Feature importance not available for this model.")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize model
    model_trainer = PricePredictionModel()
    
    # Example: Load preprocessed data and train models
    # df = pd.read_csv('data/processed/vehicles_processed.csv')
    # X = df.drop('price', axis=1)
    # y = df['price']
    # 
    # model_trainer.split_data(X, y)
    # 
    # # Train multiple models
    # model_trainer.train_linear_regression()
    # model_trainer.train_ridge_regression()
    # model_trainer.train_random_forest()
    # model_trainer.train_gradient_boosting()
    # 
    # # Evaluate all models
    # results = model_trainer.evaluate_all_models()
    # 
    # # Save the best model
    # model_trainer.save_model()
