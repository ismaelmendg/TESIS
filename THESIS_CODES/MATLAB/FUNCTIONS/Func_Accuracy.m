%%FUNCTION TO CREATE THE PRECISION MATRIX
%Acc - Variable in which the array will be created
%column - Variable that gives the change of column
%FeatTest - Feature test matrix
%Rest of data - Models of machine learning
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Accuracy(Acc,column, FeatTest, EMG_NB, EMG_SVM, EMG_DT, EMG_KNN, EMG_QDA, EMG_LDA)
    
    [A, B] = size(FeatTest);
    
    Acc(1,column)=sum(FeatTest(:,B) == EMG_NB) / A; 
    Acc(2,column)=sum(FeatTest(:,B) == EMG_SVM) / A;  
    Acc(3,column)=sum(FeatTest(:,B) == EMG_DT) / A;  
    Acc(4,column)=sum(FeatTest(:,B) == EMG_KNN) / A;   
    Acc(5,column)=sum(FeatTest(:,B) == EMG_QDA) / A;   
    Acc(6,column)=sum(FeatTest(:,B) == EMG_LDA) / A;
    
    DataOut = Acc;
    
end
