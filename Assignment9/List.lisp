
%Function

(defun list-nth (N L)
  "Return the N'th member of a list L."
  (if (null L)
      nil
    (if (zerop N) 
	(first L)
      (list-nth (1- N) (rest L)))))

%Function call
% (list-nth 2 '(a b c d))